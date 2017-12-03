import QtQuick 2.7
import "../components"

MouseArea {
    id: item
    property var book

    width: 130

    onClicked: {
        app.newWindow(Qt.resolvedUrl("../reader/ReaderWindow.qml"), { from: item, book: book })
    }

    Image {
        id: image

        anchors.centerIn: parent

        width: source.width/source.height * height
        height: parent.height - 30

        fillMode: Image.PreserveAspectFit
        source: book.cover
        mipmap: true

        layer.enabled: true
        layer.effect: Elevation {
            elevation: 2
        }
    }
}
