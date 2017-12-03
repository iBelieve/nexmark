import QtQuick 2.7
import "../components"

Column {
    property alias books: booksList.model
    // property alias pocketArticles: pocketList.model

    Header {}
    Subheader { text: "Books" }

    ListView {
        id: booksList
        anchors.left: parent.left
        anchors.right: parent.right

        height: 100
        orientation: Qt.Horizontal

        delegate: BookItem {
            book: books[index]
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
