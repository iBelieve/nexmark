import QtQuick 2.7
import "../components"

MouseArea {
    id: item
    property var book

    width: 130
    height: parent.height

    onClicked: {
        app.newWindow(Qt.resolvedUrl("../reader/ReaderWindow.qml"), { from: item, book: book })
    }

    BookCover {
        anchors.centerIn: parent

        source: book.cover
        maxSize.width: parent.width - 30
        maxSize.height: parent.height - 30

        layer.enabled: true
        layer.effect: Elevation {
            elevation: 2
        }
    }
}
