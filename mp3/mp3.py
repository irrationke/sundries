from pydub import AudioSegment
from pydub.utils import which

# 指定ffmpeg和ffprobe的路径
# ffmpeg_path = r"E:\sundries\mp3\ffmpeg-7.0.1-full_build\bin\ffmpeg.exe"
# ffprobe_path = r"E:\sundries\mp3\ffmpeg-7.0.1-full_build\bin\ffprobe.exe"

# AudioSegment.converter = which("ffmpeg.exe", path="E:\\sundries\mp3\\ffmpeg-7.0.1-full_build\\bin")
# AudioSegment.ffprobe = which("ffprobe.exe", path="E:\\sundries\mp3\\ffmpeg-7.0.1-full_build\\bin")

def extract_segment(input_file, start_time, end_time, output_file):
    """
    截取MP3文件的时间段

    参数：
    - input_file: 输入的MP3文件路径
    - start_time: 开始时间（以毫秒为单位）
    - end_time: 结束时间（以毫秒为单位）
    - output_file: 输出的MP3文件路径
    """

    # AudioSegment.converter = ffmpeg_path
    # AudioSegment.ffprobe = ffprobe_path
    # 加载音频文件
    audio = AudioSegment.from_mp3(input_file)
    
    # 截取指定时间段
    extracted_audio = audio[start_time:end_time]
    
    # 导出截取的音频
    extracted_audio.export(output_file, format="mp3")

# 示例调用
input_file = r"E:\sundries\mp3\就是南方凯 - 离别开出花.mp3"
# start_time = 60000  # 1 minute in milliseconds
start_time = 0
end_time = 95000  # 2 minutes in milliseconds 95000 -> 1m35s
output_file = r"E:\sundries\mp3\就是南方凯 - 离别开出花-1m30s.mp3"

extract_segment(input_file, start_time, end_time, output_file)
