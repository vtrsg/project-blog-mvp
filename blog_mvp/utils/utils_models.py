import os

def upload_image_to(instance, filename):
    post_id = instance.id
    extension = filename.split('.')[1]
    new_filename = f'post_{post_id}.{extension}'
    return os.path.join(str(instance.created_at.year), str(instance.created_at.month), new_filename)