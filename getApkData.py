import os
import platform
import argparse

from lib.ApkDownloader import FileDownloader, FileExtractor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download & extract Blue Archive XAPK and Il2CppDumper"
    )
    parser.add_argument(
        "--region",
        choices=["global", "jp"],
        default="jp",
        help="Which region APK to download (default: jp)",
    )
    args = parser.parse_args()
    region = args.region

    lib_dir = os.path.join(os.getcwd(), f'dump_lib')
    download_dir = os.path.join(os.getcwd(), f'{region}_download')
    extract_dir = os.path.join(os.getcwd(), f'{region}_extracted')
    os_system = platform.system()

    if region == "global":
        pkg = "com.nexon.bluearchive"
    else:
        pkg = "com.YostarJP.BlueArchive"

    # Download the required dumper
    il2cppDumperUrl = "https://github.com/AndnixSH/Il2CppDumper/releases/download/v6.7.46/Il2CppDumper-net8-linux-x64-v6.7.46.zip"
    if os_system == "Windows":
        il2cppDumperUrl = "https://github.com/Perfare/Il2CppDumper/releases/download/v6.7.46/Il2CppDumper-net6-v6.7.46.zip"
    il2cppDownloader = FileDownloader(il2cppDumperUrl, lib_dir, "il2cppDumper.zip")
    il2cppDownloader.download()
    FileExtractor(il2cppDownloader.local_filepath, lib_dir, "").extract_il2cpp()

    fbsDumperUrl = "https://github.com/ArkanDash/FbsDumperV2/releases/download/1.0.0/FbsDumper-net8-linux-x64.zip"
    if os_system == "Windows":
        fbsDumperUrl = "https://github.com/ArkanDash/FbsDumperV2/releases/download/1.0.0/FbsDumper-net8-win-x64.zip"
    fbsDumperDownload = FileDownloader(fbsDumperUrl, lib_dir, "fbsDumper.zip")
    fbsDumperDownload.download()
    FileExtractor(fbsDumperDownload.local_filepath, lib_dir, "").extract_fbsdumper()
    print("Successfully downloaded and extracted the required dumper")

    # Download and Extract the Game XAPK
    print(f"Downloading {region} APK...")
    xapk_url = f"https://d.apkpure.com/b/XAPK/{pkg}?version=latest"
    downloader = FileDownloader(xapk_url, download_dir, "BlueArchive.xapk")
    downloader.download()
    FileExtractor(downloader.local_filepath, extract_dir, region).extract_xapk()

    print("Successfully downloaded and extracted files")