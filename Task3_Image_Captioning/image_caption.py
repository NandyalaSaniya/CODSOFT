import os

print("=" * 55)
print("🖼️ IMAGE CAPTIONING SYSTEM")
print("=" * 55)

captions = {
    "cat": "A cute cat sitting comfortably and looking at the camera.",
    "dog": "A playful dog enjoying time in the park.",
    "car": "A modern car parked beside the road.",
    "tree": "A beautiful green tree in a natural environment.",
    "flower": "A colorful flower blooming in the garden.",
    "bird": "A bird resting on a tree branch.",
    "house": "A house surrounded by greenery.",
    "person": "A person standing and smiling at the camera.",
    "laptop": "A laptop placed on a study desk.",
    "phone": "A smartphone kept on a table."
}

image_name = input("\nEnter image file name (example: cat.jpg): ").lower()

file_name = os.path.splitext(image_name)[0]

found = False

for keyword in captions:
    if keyword in file_name:
        print("\n📌 Generated Caption:")
        print(captions[keyword])
        found = True
        break

if not found:
    print("\n📌 Generated Caption:")
    print("An image containing various objects and scenery.")

print("\n✅ Caption generation completed.")