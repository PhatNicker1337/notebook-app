from core import Notebook


def main():
    notebook = Notebook()
    print("📓 Notebook App PhatNicker1337")

    while True:
        print("\n1: Add note  2: List notes  3: Delete note  4: Exit")
        choice = input("Choice: ")

        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            notebook.add_note(title, content)
            print("✅ Note added!")

        elif choice == '2':
            notes = notebook.list_notes()
            for note in notes:
                print(f"{note['id']}. {note['title']}: {note['content']}")

        elif choice == '3':
            note_id = int(input("Note ID to delete: "))
            notebook.delete_note(note_id)
            print("✅ Note deleted!")

        elif choice == '4':
            break


if __name__ == "__main__":
    main()