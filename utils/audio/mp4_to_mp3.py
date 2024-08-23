"""
Desc:批量mp4转mp4
Usage: 修改mp4/mp3文件夹路径

pip install moviepy pydub
"""


import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from multiprocessing import Pool, cpu_count

def convert_file(file_info):
    input_file, output_file = file_info
    
    # 使用 moviepy 从 MP4 文件中提取音频
    video = VideoFileClip(input_file)
    audio = video.audio
    temp_audio_file = input_file.replace(".mp4", ".wav")
    audio.write_audiofile(temp_audio_file)
    
    # 使用 pydub 将 WAV 文件转换为 MP3 文件
    audio_segment = AudioSegment.from_wav(temp_audio_file)
    audio_segment.export(output_file, format="mp3")
    
    # 删除临时的 WAV 文件
    os.remove(temp_audio_file)
    
    print(f"Converted {input_file} to {output_file}")

def convert_mp4_to_mp3(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取所有 MP4 文件的路径和对应的输出路径
    file_info_list = [
        (os.path.join(input_folder, file_name), os.path.join(output_folder, file_name.replace(".mp4", ".mp3")))
        for file_name in os.listdir(input_folder) if file_name.endswith(".mp4")
    ]
    
    # 使用多进程池来并行处理文件转换
    with Pool(cpu_count()) as pool:
        pool.map(convert_file, file_info_list)

if __name__ == "__main__":
    input_folder = "mp4_folder"  # 替换为你的输入 MP4 文件夹路径
    output_folder = "mp3_folder"  # 替换为你的输出 MP3 文件夹路径
    convert_mp4_to_mp3(input_folder, output_folder)
