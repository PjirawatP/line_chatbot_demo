import os
from dotenv import load_dotenv

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, AudioMessageContent, FileMessageContent, ImageMessageContent, LocationMessageContent, StickerMessageContent, TextMessageContent, VideoMessageContent

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.services.conversation import save_conversation
from src.config.database import create_db_and_tables
from src.services.user import get_user
from src.services.response import chatbot_response


app = FastAPI()


origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


load_dotenv()

configuration = Configuration(access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(channel_secret = os.getenv("LINE_CHANNEL_SECRET"))


@app.post("/callback")
async def callback(request: Request):
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = await request.body()
    body = body.decode("utf-8")

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return JSONResponse(
            status_code = 400,
            content = {
                "status": 0,
                "message": "Invalid signature. Please check your channel access token/channel secret.",
                "data": {}
            }
        )

    return "OK"


@handler.add(MessageEvent, message = AudioMessageContent)
def handle_audio_message(event):
    response = "ขออภัยในความไม่สะดวก ระบบรองรับเฉพาะข้อความที่เป็นตัวอักษรเท่านั้น" 

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )


@handler.add(MessageEvent, message = FileMessageContent)
def handle_file_message(event):
    response = "ขออภัยในความไม่สะดวก ระบบรองรับเฉพาะข้อความที่เป็นตัวอักษรเท่านั้น" 

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )


@handler.add(MessageEvent, message = ImageMessageContent)
def handle_image_message(event):
    response = "ขออภัยในความไม่สะดวก ระบบรองรับเฉพาะข้อความที่เป็นตัวอักษรเท่านั้น" 

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )


@handler.add(MessageEvent, message = LocationMessageContent)
def handle_location_message(event):
    response = "ขออภัยในความไม่สะดวก ระบบรองรับเฉพาะข้อความที่เป็นตัวอักษรเท่านั้น" 

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )


@handler.add(MessageEvent, message = StickerMessageContent)
def handle_sticker_message(event):
    response = "ขออภัยในความไม่สะดวก ระบบรองรับเฉพาะข้อความที่เป็นตัวอักษรเท่านั้น" 

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )


@handler.add(MessageEvent, message = TextMessageContent)
def handle_text_message(event):
    user_id = event.source.user_id
    user_message = event.message.text

    user = get_user(user_id)

    response = chatbot_response(user_id, user_message)

    if response == "":
        response = "ขออภัยในความไม่สะดวก ระบบไม่สามารถใชังานได้ในขณะนี้"
    else:
        save_conversation(user_id, user_message, response)

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )


@handler.add(MessageEvent, message = VideoMessageContent)
def handle_video_message(event):
    response = "ขออภัยในความไม่สะดวก ระบบรองรับเฉพาะข้อความที่เป็นตัวอักษรเท่านั้น" 

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token = event.reply_token,
                messages = [TextMessage(text = response)]
            )
        )
