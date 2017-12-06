import QtQuick 2.7
import io.mspencer.Nexmark 1.0
import "../components"

Column {
    id: column

    Header {
        id: header
    }

    GridView {
        id: grid
        height: parent.height - header.height
        width: parent.width

        model: BooksManager.books

        cellWidth: grid.width/4
        cellHeight: cellWidth * 1.3
        clip: true

        delegate: BookItem {
            book: BooksManager.bookAt(index)
            width: grid.cellWidth
            height: grid.cellHeight
        }

        Scrollbar {
            flickable: grid
        }
    }

    // ListSection {
    //     id: booksList
    //     title: "Books"
    //     placeholder: "No books yet"

    //     itemHeight: 180
    //     model: BooksManager.books

    //     delegate: BookItem {
    //         book: model
    //     }
    // }

    // ListSection {
    //     title: "Recent Notes"
    //     itemHeight: 180
    //     model: [
    //         // { title: "Sample Note", contents: "Note contents goes here:\n • Here is a bullet point" }
    //         { title: "Sample Note", contents: "Note contents goes here:<ul><li>Here is a bullet point</li></ul>" }
    //     ]

    //     delegate: NoteItem {
    //         note: modelData
    //     }
    // }

    // Subheader { text: "Articles" }

    // ListView {
    //     id: pocketList
    //     anchors.left: parent.left
    //     anchors.right: parent.right

    //     height: 100
    //     orientation: Qt.Horizontal

    //     delegate: PocketItem {
    //         book: pocketArticles[index]
    //     }
    // }
}
