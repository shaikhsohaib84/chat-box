from email import message
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_name = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Create group
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
        )
    
        await self.accept()

    async def disconnect(self, self_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    
    async def receive(self, text_data=None, bytes_data=None):
        test_data_json = json.loads(text_data)
        
        message = test_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                
            }
        )
    
    async def chat_message(self, event):
        
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
            
        }))