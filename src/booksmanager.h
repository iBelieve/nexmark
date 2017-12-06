#pragma once

#include <QtCore/QObject>
#include <QtCore/QUrl>
#include <QtQml/QQmlEngine>
#include <QtQml/QQmlListProperty>
#include <QtSql/QSqlDatabase>
#include <QtCore/QDebug>

class Book;

class BooksManager : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QQmlListProperty<Book> books READ books NOTIFY booksChanged)

public:
    BooksManager(QObject *parent = nullptr);

    static QObject *qmlSingleton(QQmlEngine *engine, QJSEngine *scriptEngine);

    QQmlListProperty<Book> books() {
        return QQmlListProperty<Book>(this, m_books);
    }

    Q_INVOKABLE Book *bookAt(int index) const {
        return m_books[index];
    }

public slots:
    void refresh();

signals:
    void booksChanged();

private:
    QList<Book *> m_books;
    QSqlDatabase m_db;
};
