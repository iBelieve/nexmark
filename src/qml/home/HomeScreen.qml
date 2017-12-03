import QtQuick 2.7
import io.mspencer.Nexmark 1.0
import "../components"

Column {
    id: column

    Header {}

    ListSection {
        id: booksList
        title: "Books"
        placeholder: "No books yet"

        itemHeight: 180
        model: BooksManager.books

        delegate: BookItem {
            book: model
            height: booksList.itemHeight
        }
    }

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
