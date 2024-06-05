import uvicorn
from nestipy.core import NestipyFactory
from nestipy.openapi import DocumentBuilder, SwaggerModule

from app_module import AppModule

app = NestipyFactory.create(AppModule)

document = DocumentBuilder().set_title("Nestipy JWT").set_description("Nestipy JWT endpoint").add_bearer_auth().build()
SwaggerModule.setup('api', app, document)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
