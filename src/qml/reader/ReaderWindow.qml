import QtQuick 2.7
import ".."

Window {
    property var book

    Image {
        id: image

        anchors.centerIn: parent

        width: sourceSize.width/sourceSize.height * height
        height: Utils.translate(parent.height,
                                from.height, app.height,
                                from.height, Math.min(sourceSize.height, app.height - 100))

        fillMode: Image.PreserveAspectFit
        source: book.cover
        mipmap: true
    }
}
