
# wall_location = '/home/nik/Pictures/wallpapers/Fantasy-Lake5.png'
# hyprlock_conf_path = '/home/nik/Downloads/hyprlock.conf'

def lock_wall_match(path_to_hyprlock_conf, new_wallpaper_location):
    with open(path_to_hyprlock_conf, 'r+') as f:
        # reading all contents
        contents_list = f.readlines()
        # remember the index of the line i want to replace
        path_strs_dict = {i:v for i,v in enumerate(contents_list) if ('path') in v}
        # save the index
        in_loc_req_path = min(list(path_strs_dict.keys()))
        # get the exact string
        path_str = path_strs_dict[in_loc_req_path]
        # split the line to get the path string
        sep_str = path_str.split(' ')
        # remove the old path
        sep_str.pop()
        # insert the new path
        sep_str.append(new_wallpaper_location)
        # make the entire line again
        final_path = ' '.join(sep_str)
        # add a new line char  
        line_to_add = final_path + '\n'
        contents_list[in_loc_req_path] = line_to_add
        # adding seek because after reading the file the cursor is at the end so doing truncate does nothing, take the cursor to start of file and then do truncate
        f.seek(0)
        f.truncate()
        f.writelines(contents_list)

# lock_wall_match(hyprlock_conf_path, wall_location)
