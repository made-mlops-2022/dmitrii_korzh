import os
from typing import List

import uvicorn
from fastapi import FastAPI

from src.utils.utils import HeartDiseaseModel, ModelResponse
from src.utils.utils import downoload_checkpoints, create_logger, load_config, load_object
from src.utils.utils import prediction, create_inference_pipeline

from src.utils.scaler import CustomScaler
from src.utils.predict_config import return_predict_config
from pathlib import Path
import gdown


GDOWN_ID = "1Noc5ld0vzXBGzL-6AXGUjToSy_q_VeO5"


app = FastAPI()
config = load_config()
# log_config = return_predict_config()
logger = create_logger('online_inference', config['logging'])
model = None
transformer = None

@app.on_event('startup')
def load_model():
    logger.info('Loading model')
    model_path = config['model_path']
    my_file = Path(config['model_path'])
    if not my_file.is_file():
        error = (f'There is no {model_path}, trying to downoload')
        logger.error(error)
        gdown.download(id=GDOWN_ID, output=model_path, quiet=False)
        my_file = Path(config['model_path'])
        if not my_file.is_file():
            error = (f'There is no {model_path}, downoloadidg didnt help')
            logger.error(error)
            raise RuntimeError(error)

    global model, transformer
    model = load_object(model_path)
    logger.info(f'Model is loaded')
    
    
@app.get('/')
async def root():
    return {'message': 'Hello'}


@app.post('/predict', response_model=List[ModelResponse]) 
async def predict(request: HeartDiseaseModel):
    logger.info("Making predictions")
    preds = prediction(request.data, request.feature_names, model)
    return preds
    
    
@app.get('/health')
async def health_check():
    if model:
        return 200


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT", 8112))
