# In file: frontend/api/chat.py

import os
import json
import google.generativeai as genai
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        # 1. Read the incoming data from your .exe application
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data)

        # 2. Extract all the necessary pieces of data from the payload
        user_message = payload.get('message', '')
        conversation_history = payload.get('history', [])
        user_name = payload.get('user_name', 'friend') # Default value 'friend'
        user_stats = payload.get('stats', {}) # Default to empty dict for safety

        try:
            # 3. Securely get the API key from Vercel's Environment Variables
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY environment variable not set on Vercel!")

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            # 4. Build the full, detailed prompt using the data received
            conversation_history.append(f"User: {user_message}")
            history_for_prompt = "\n".join(conversation_history)

            # --- YOUR DETAILED PROMPT LIVES HERE, ON THE SERVER ---
            prompt = f"""
            You are DrishtiAI, a gentle and supportive wellness companion. Your user's name is {user_name}.

            Core Identity:
            - You ARE DrishtiAI. Do not introduce yourself in every message. Assume the user knows who you are.
            - Your tone is always warm, empathetic, and kind, like a caring friend.
            - You are capable of answering general knowledge questions, but always try to gently guide the conversation back to wellness, well-being, or your core functionalities.

            This is the recent conversation history:
            {history_for_prompt}

            User's NEW Message: "{user_message}"

            Context Data (Only use if relevant to the conversation):
            - Average Blink Rate: {user_stats.get('avg_bpm', 'N/A')} BPM
            - Screen Health Score: {user_stats.get('health_score', 'N/A')}/100
            - Common Fatigue Time: {user_stats.get('fatigue_hotspot_hour', 'N/A')}

            Behavior Rules:
            - If the user sounds stressed or tired, respond with calming and reassuring words. Offer a simple breathing exercise.
            - If the user sounds happy, match their energy with light, encouraging, and slightly playful support.
            - If the user asks a factual question that is NOT directly related to wellness (e.g., "who is X?", "what is Y?"), answer it concisely and accurately. After answering, gently pivot back to their well-being or offer a wellness tip.
            - If the user's message is unclear, gibberish, or just a simple greeting, respond with a gentle check-in.
            - Be concise. Keep your replies to 2-3 short sentences.
            - Avoid using the user's name({user_name}) repeatedly.
            """

            # 5. Call the Gemini API and get the response
            response = model.generate_content(prompt)
            bot_reply = response.text
            conversation_history.append(f"AI: {bot_reply}")

            # 6. Send the response and updated history back to your .exe
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_payload = json.dumps({'reply': bot_reply, 'history': conversation_history})
            self.wfile.write(response_payload.encode('utf-8'))

        except Exception as e:
            print(f"[VERCEL FUNCTION ERROR] API call failed: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_payload = json.dumps({'reply': 'Sorry, the AI service seems to be having issues right now.'})
            self.wfile.write(error_payload.encode('utf-8'))

        return