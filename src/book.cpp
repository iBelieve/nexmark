#include "book.h"

#include <QtCore/QDir>
#include <QtSql/QSqlQuery>
#include <QtSql/QSqlError>
#include <QtCore/QDebug>

#include "booksmanager.h"

Book::Book(int id, QString title, QString path, bool hasCover, QObject *parent)
    : QObject(parent), id(id), title(title), path(path), hasCover(hasCover)
{}

QUrl Book::cover() const
{
    if (hasCover) {
        return QUrl::fromLocalFile(path + "/cover.jpg");
    } else {
        return QUrl();
    }
}

QString Book::filename(const QString &format) {
    QSqlQuery query("SELECT name FROM data WHERE book = ? AND format = ?");
    query.addBindValue(id);
    query.addBindValue(format);

    if (!query.exec()) {
        qWarning() << "Unable to fetch format:" << query.lastError().text();
        return QString();
    }

    query.first();

    if (!query.isValid()) {
        qDebug() << "Format not available:" << format;
        return QString();
    }

    auto name = query.value(0).toString();
    auto filename = path + "/" + name + "." + format.toLower();

    return filename;
}
