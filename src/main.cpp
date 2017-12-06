#include <QtGui/QGuiApplication>
#include <QtQml/QQmlApplicationEngine>

#include "book.h"
#include "booksmanager.h"
#include "epubfile.h"

int main(int argc, char *argv[])
{
    // QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
    QGuiApplication app(argc, argv);

    const char *uri = "io.mspencer.Nexmark";

    qmlRegisterSingletonType<BooksManager>(uri, 1, 0, "BooksManager", BooksManager::qmlSingleton);
    qmlRegisterUncreatableType<Book>(uri, 1, 0, "Book", QStringLiteral("Accessed via BooksManager"));
    qmlRegisterType<EPUBFile>(uri, 1, 0, "EPUBFile");

    QQmlApplicationEngine engine(QUrl(QStringLiteral("qrc:/qml/Main.qml")));

    return app.exec();
}
