import requests
import time
import os

def remove_bg(img_bg_color: str, image_path: str) -> dict:
    this_script_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(
        'output',
    )
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # do remove background api
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(image_path, 'rb')},
        data={'size': 'auto', 'bg_color': img_bg_color},
        headers={'X-Api-Key': os.environ['API_KEY_RM_BG']},
    )
    if response.status_code == requests.codes.ok:
        output_name = f"{time.time()}.png"
        ouput_path = os.path.join(
            output_dir,
            output_name
        )
        with open(ouput_path, 'wb') as out:
            out.write(response.content)
        print(f"Check image in {ouput_path}")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    remove_bg(
        image_path='images/sample_foto.jpeg',
        img_bg_color='red'
    )