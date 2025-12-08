# notion_client.py
import os
import requests
from typing import Dict, Any

class NotionClient:
    def __init__(self):
        self.api_key = os.getenv("NOTION_API_KEY")
        self.database_id = os.getenv("NOTION_DATABASE_ID")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
    
    def create_page(self, data: Dict[str, Any]) -> Dict:
        """Notion 데이터베이스에 페이지 생성"""
        url = "https://api.notion.com/v1/pages"
        
        # properties 구조: 각 필드 타입에 맞게 작성
        payload = {
            "parent": {
                "type": "database_id",
                "database_id": self.database_id
            },
            "properties": {
                "회사명": {  # Title 타입
                    "title": [
                        {
                            "text": {
                                "content": data.get("company", "")
                            }
                        }
                    ]
                },
                "포지션": {  # Rich text 타입
                    "rich_text": [
                        {
                            "text": {
                                "content": data.get("position", "")
                            }
                        }
                    ]
                },
                "위치": {
                    "rich_text": [
                        {
                            "text": {
                                "content": data.get("location", "")
                            }
                        }
                    ]
                },
                "연봉": {
                    "rich_text": [
                        {
                            "text": {
                                "content": data.get("salary", "")
                            }
                        }
                    ]
                },
                "경력": {
                    "rich_text": [
                        {
                            "text": {
                                "content": data.get("experience", "")
                            }
                        }
                    ]
                },
                "필수 스킬": {  # Multi-select 타입
                    "multi_select": [
                        {"name": skill} for skill in data.get("required_skills", [])
                    ]
                },
                "우대 스킬": {
                    "multi_select": [
                        {"name": skill} for skill in data.get("preferred_skills", [])
                    ]
                },
                "상태": {  # Select 타입
                    "select": {
                        "name": "지원 전"
                    }
                }
            }
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"에러: {response.status_code}")
            print(response.json())
            return None