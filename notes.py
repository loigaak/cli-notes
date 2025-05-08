import argparse
import json
import os
from datetime import datetime

DATA_FILE = 'notes.json'

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_notes(notes):
    with open(DATA_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note(content):
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({'id': note_id, 'content': content, 'timestamp': timestamp})
    save_notes(notes)
    print(f"Note added with ID: {note_id}")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f"ID: {note['id']}, Content: {note['content']}, Timestamp: {note['timestamp']}")

def search_notes(keyword):
    notes = load_notes()
    found = [note for note in notes if keyword.lower() in note['content'].lower()]
    if not found:
        print("No notes found with that keyword.")
        return
    for note in found:
        print(f"ID: {note['id']}, Content: {note['content']}, Timestamp: {note['timestamp']}")

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print(f"Note with ID: {note_id} deleted.")

def main():
    parser = argparse.ArgumentParser(description="CLI Note-Taking App")
    subparsers = parser.add_subparsers(dest='command')

    # Add note
    add_parser = subparsers.add_parser('add', help='Add a new note')
    add_parser.add_argument('content', type=str, help='Content of the note')

    # List notes
    subparsers.add_parser('list', help='List all notes')

    # Search notes
    search_parser = subparsers.add_parser('search', help='Search notes by keyword')
    search_parser.add_argument('keyword', type=str, help='Keyword to search for')

    # Delete note
    delete_parser = subparsers.add_parser('delete', help='Delete a note by ID')
    delete_parser.add_argument('id', type=int, help='ID of the note to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_note(args.content)
    elif args.command == 'list':
        list_notes()
    elif args.command == 'search':
        search_notes(args.keyword)
    elif args.command == 'delete':
        delete_note(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
