#include "booksmanager.h"

#include <QtSql/QSqlQuery>
#include <QtSql/QSqlError>
#include <QtCore/QDir>
#include <QtCore/QDebug>

QUrl Book::cover() const
{
    if (hasCover) {
        return QUrl::fromLocalFile(QDir::homePath() + "/Books/" + path + "/cover.jpg");
    } else {
        return QUrl();
    }
}

BooksManager::BooksManager(QObject *parent)
    : QObject(parent)
{
    m_db = QSqlDatabase::addDatabase("QSQLITE");
    m_db.setDatabaseName(QDir::homePath() + "/Books/metadata.db");

    if (m_db.open()) {
        refresh();
    } else {
        qWarning("Unable to open database");
    }
}

QObject *BooksManager::qmlSingleton(QQmlEngine *engine, QJSEngine *scriptEngine) {
    Q_UNUSED(scriptEngine)

    return new BooksManager(engine);
}

void BooksManager::refresh()
{
    QSqlQuery query;

    if (!query.exec("SELECT id, title, path, has_cover FROM books")) {
        qWarning("Unable to fetch books: %s", qPrintable(query.lastError().text()));
    }

    qDeleteAll(m_books);
    m_books.clear();

    while (query.next()) {
        auto id = query.value(0).toInt();
        auto title = query.value(1).toString();
        auto path = query.value(2).toString();
        auto hasCover = query.value(3).toBool();

        m_books += new Book(id, title, path, hasCover, this);
    }

    emit booksChanged();
}
