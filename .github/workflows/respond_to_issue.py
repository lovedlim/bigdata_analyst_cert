import os
import openai
import requests

# GitHub 환경 변수 설정
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('GITHUB_REPOSITORY')
ISSUE_NUMBER = os.getenv('ISSUE_NUMBER')
COMMENT_BODY = os.getenv('COMMENT_BODY')
COMMENT_AUTHOR = os.getenv('COMMENT_AUTHOR')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = OPENAI_API_KEY

# 이슈의 제목, 본문, 그리고 모든 댓글 가져오기
def get_issue_and_comments():
    issue_url = f"https://api.github.com/repos/{REPO_NAME}/issues/{ISSUE_NUMBER}"
    comments_url = f"https://api.github.com/repos/{REPO_NAME}/issues/{ISSUE_NUMBER}/comments"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    # 이슈 정보 가져오기
    issue_response = requests.get(issue_url, headers=headers)
    print(f"Issue API response status: {issue_response.status_code}")
    
    if issue_response.status_code == 200:
        issue_data = issue_response.json()
        issue_title = issue_data.get('title', '')
        issue_body = issue_data.get('body', '')
    else:
        print("Failed to fetch issue data from GitHub API.")
        return None, None, None

    # 이슈의 모든 댓글 가져오기
    comments_response = requests.get(comments_url, headers=headers)
    print(f"Comments API response status: {comments_response.status_code}")
    
    if comments_response.status_code == 200:
        comments_data = comments_response.json()
        comments = [f"{comment['user']['login']} said: {comment['body']}" for comment in comments_data]
    else:
        print("Failed to fetch comments from GitHub API.")
        return issue_title, issue_body, None

    return issue_title, issue_body, comments

# ChatGPT API 호출
def get_chatgpt_response(title, body, comments, new_comment):
    try:
        # 프롬프트 생성: 제목, 본문, 기존 댓글, 새 댓글
        prompt = f"Title: {title}\n\nBody: {body}\n\nComments:\n"
        if comments:
            prompt += "\n".join(comments)
        if new_comment:
            prompt += f"\n\nNew comment from {COMMENT_AUTHOR}: {new_comment}\n\nRespond to the new comment:"
        else:
            prompt += "\n\nRespond to the issue:"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2024  # 필요에 따라 조정
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

# 이슈 댓글에 답글 추가
def comment_on_issue(response):
    if not response:
        print("No response to post.")
        return

    url = f"https://api.github.com/repos/{REPO_NAME}/issues/{ISSUE_NUMBER}/comments"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"body": response}
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print("Response posted successfully.")
    else:
        print(f"Failed to post response. Status code: {response.status_code}, Response: {response.text}")

def main():
    issue_title, issue_body, comments = get_issue_and_comments()
    if issue_title and issue_body:  # 제목과 본문이 모두 있을 때만 응답 생성
        response = get_chatgpt_response(issue_title, issue_body, comments, COMMENT_BODY)
        print(f"Generated response: {response}")  # 디버깅용 출력
        comment_on_issue(response)
    else:
        print("No issue title or body found.")

if __name__ == "__main__":
    main()
