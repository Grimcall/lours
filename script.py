import random

# Simulate content items with random titles and types
content_items = [
    {"id": i, "title": f"Content {i}", "content_type": random.choice(["text", "image", "note", "video"])}
    for i in range(1, 6)  # Generate 10 items for testing
]

# Initialize two lists for the two columns
page1 = []
page2 = []

# Distribute content items between the two columns
reversed_content_items = content_items[::-1]
mid_index = len(reversed_content_items) // 2
if len(reversed_content_items) % 2 != 0:
    mid_index += 1
page1 = reversed_content_items[:mid_index]
page2 = reversed_content_items[mid_index:]

print("List of items: ")

for item in content_items:
    print(item)

print("\nPage 1:")
for item in page1:
    print(item)

print("\nPage 2:")
for item in page2:
    print(item)
