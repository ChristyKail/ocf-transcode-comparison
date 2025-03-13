
#!/usr/bin/env python3

import DaVinciResolveScript as dvrs

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

resolve_conn = dvrs.scriptapp("Resolve")

project_manager = resolve_conn.GetProjectManager()
project = project_manager.GetCurrentProject()
media_pool = project.GetMediaPool()

media_pool.SetCurrentFolder(media_pool.GetRootFolder())

root_subfolders = media_pool.GetRootFolder().GetSubFolderList()

ocf_folder = None
transcode_folder = None


for folder in root_subfolders:

    name = folder.GetName()
    if name == "TRANS":
        transcode_folder = folder
    elif name == "OCF":
        ocf_folder = folder

if not ocf_folder or not transcode_folder:
    print("Invalid bin structure for this script to run")
    exit(1)

ocf_clips = ocf_folder.GetClipList()
transcode_clips = transcode_folder.GetClipList()

print(ocf_clips, transcode_clips)

ocf_tl = media_pool.CreateTimelineFromClips("OCF_Clips", ocf_clips)
transcode_tl = media_pool.CreateTimelineFromClips("Transcode_Clips", transcode_clips)

ocf_frames = ocf_tl.GetEndFrame()
transcode_frames = transcode_tl.GetEndFrame()

if ocf_frames == transcode_frames:
    print(bcolors.OKGREEN)

else:
    print(bcolors.FAIL)

print(f"OCF Frames: {ocf_frames}")
print(f"Transcode Frames: {transcode_frames}")
print(bcolors.ENDC)

media_pool.DeleteTimelines([ocf_tl, transcode_tl])