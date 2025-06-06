input_notes = input("Enter notes separated by commas: ")
notes = [note.strip() for note in input_notes.split(',') if note.strip()]
# Sort the notes alphabetically
if not notes:
    print("No notes provided.")
    exit()

sorted_notes = sorted(notes)
for note in sorted_notes:
    print(note)
       
# Save the sorted notes to a file
with open("sorted_notes.txt", "w") as file:
    for note in sorted_notes:
        file.write(note + "\n")
print("Sorted notes have been saved to 'sorted_notes.txt'.")
# This script sorts a list of notes alphabetically and saves the sorted list to a file.
