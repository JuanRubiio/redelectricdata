from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn
import router, config


settings = config.get_settings()
env_root_path = settings.env_root_path_local if settings.ENV_VAR == 'local' else settings.env_root_path_dev

app_config = {
    
    'title': settings.app_name,
    'description': settings.app_description,
    'version': settings.app_version,
    'docs_url':'/docs',
    'redocs_url':'/redocs',
    'contact':{
        'name':settings.dev_name,
        'email':settings.dev_email,   
    },
    
}

app = FastAPI(**app_config)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)

app.include_router(router.api_router, prefix='/api',)
if env_root_path:app.mount(env_root_path, app)

if __name__=="__main__":
    uvicorn.run("main:app", host=settings.app_host, port=settings.app_port, reload=settings.app_deamon, log_level=settings.app_log_level, debug=settings.app_debug_mode)

