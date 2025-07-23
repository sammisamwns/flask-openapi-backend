#!/usr/bin/env python3
"""
Test script for the Flask OpenAI API
Run this to test your API setup
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Check if API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "your-openai-key-here":
    print("❌ Error: Please set your OpenAI API key in the .env file")
    print("Get your key from: https://platform.openai.com/api-keys")
    exit(1)

# Test configuration
BASE_URL = "http://localhost:5000"
TEST_PROMPT = "Write a short poem about artificial intelligence"

def test_chat_mode():
    """Test the chat mode endpoint"""
    print("🧪 Testing Chat Mode (GPT-4o-mini)...")
    
    payload = {
        "prompt": TEST_PROMPT,
        "mode": "chat"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/generate", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Chat mode test successful!")
            print(f"Response: {data['response'][:100]}...")
            return True
        else:
            print(f"❌ Chat mode test failed: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure the Flask server is running on localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_completion_mode():
    """Test the completion mode endpoint"""
    print("\n🧪 Testing Completion Mode (GPT-3.5-turbo)...")
    
    payload = {
        "prompt": TEST_PROMPT,
        "mode": "completion"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/generate", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Completion mode test successful!")
            print(f"Response: {data['response'][:100]}...")
            return True
        else:
            print(f"❌ Completion mode test failed: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure the Flask server is running on localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_error_handling():
    """Test error handling with invalid request"""
    print("\n🧪 Testing Error Handling...")
    
    payload = {
        "prompt": "",  # Empty prompt
        "mode": "invalid_mode"  # Invalid mode
    }
    
    try:
        response = requests.post(f"{BASE_URL}/generate", json=payload)
        
        if response.status_code == 500:
            print("✅ Error handling test successful!")
            return True
        else:
            print(f"❌ Error handling test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error handling test error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Flask OpenAI API Test Suite")
    print("=" * 40)
    
    # Run tests
    chat_success = test_chat_mode()
    completion_success = test_completion_mode()
    error_success = test_error_handling()
    
    print("\n" + "=" * 40)
    print("📊 Test Results:")
    print(f"Chat Mode: {'✅ PASS' if chat_success else '❌ FAIL'}")
    print(f"Completion Mode: {'✅ PASS' if completion_success else '❌ FAIL'}")
    print(f"Error Handling: {'✅ PASS' if error_success else '❌ FAIL'}")
    
    if all([chat_success, completion_success, error_success]):
        print("\n🎉 All tests passed! Your API is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the error messages above.") 