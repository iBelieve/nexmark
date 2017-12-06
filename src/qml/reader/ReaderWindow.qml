import QtQuick 2.7
import io.mspencer.Nexmark 1.0
import ".."
import "../components"

Window {
    id: window

    property var book

    onBookChanged: epub.load(book.filename())

    EPUBFile {
        id: epub
    }

    BookCover {
        id: cover

        anchors.centerIn: parent

        maxSize.height: app.height - 100

        width: implicitWidth * height/implicitHeight
        height: Utils.translate(parent.height,
                                        from.height, app.height,
                                        from.height, app.height - 100)

        source: book.cover
    }
}
