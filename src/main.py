from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import router
import config

settings = config.get_settings()
env_root_path = settings.env_root_path_local if settings.ENV_VAR == 'local' else settings.env_root_path_dev

app_config = {
    
    'title': settings.app_name,
    'description': settings.app_description,
    'version': settings.app_version,
    'docs_url':'/docs',
    'redocs_url':'/redocs',
    
}

app = FastAPI(**app_config)

app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
)

app.include_router(router.api_router, prefix='/api',)
if env_root_path:app.mount(env_root_path, app)

if __name__=="__main__":
    uvicorn.run("main:app", host=settings.app_host, port=settings.app_port, reload=settings.app_deamon, log_level=settings.app_log_level, debug=settings.app_debug_mode)

