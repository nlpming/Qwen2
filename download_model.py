from huggingface_hub import hf_hub_download, list_repo_files

def download_all_files(repo_id, cache_dir):
    # 获取 repo 中所有的文件列表
    all_files = list_repo_files(repo_id=repo_id)

    # 遍历文件列表，下载每一个文件
    for file_name in all_files:
        try:
            file_path = hf_hub_download(repo_id=repo_id, filename=file_name, cache_dir=cache_dir)
            print(f"Downloaded: {file_name} to {file_path}")
        except Exception as e:
            print(f"Failed to download {file_name}: {str(e)}")

# 使用示例
repo_id = "Qwen/Qwen2-0.5B-Instruct"
cache_dir = "./models"
download_all_files(repo_id, cache_dir)


