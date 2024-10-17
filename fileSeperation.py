import os
import shutil
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    """
    Parses the XML file and returns a dictionary mapping image names to their defects.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    image_defects = {}

    for defect in root.findall('Defect'):
        image_name = defect.get('name')
        defects = {child.tag for child in defect if child.text == '1'}
        image_defects[image_name] = defects

    return image_defects

def organize_images(image_defects, source_folder, destination_folder):
    """
    Organizes images into folders based on their defects, skipping images that are not found.
    """
    for image_name, defects in image_defects.items():
        source_path = os.path.join(source_folder, image_name)
        if not os.path.exists(source_path):
            print(f"Warning: Image '{image_name}' not found in '{source_folder}'. Skipping.")
            continue

        for defect in defects:
            defect_folder = os.path.join(destination_folder, defect)
            if not os.path.exists(defect_folder):
                os.makedirs(defect_folder)
            destination_path = os.path.join(defect_folder, image_name)
            shutil.copy(source_path, destination_path)

def main():
    xml_file = 'defects.xml'  # Replace with the path to your XML file
    source_folder = 'defects'               # The folder where the original images are stored
    destination_folder = 'sorted_images'    # The folder where images will be organized

    image_defects = parse_xml(xml_file)
    organize_images(image_defects, source_folder, destination_folder)

if __name__ == "__main__":
    main()
