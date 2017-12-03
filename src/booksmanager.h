#pragma once

#include <QtCore/QObject>
#include <QtCore/QUrl>
#include <QtQml/QQmlEngine>
#include <QtQml/QQmlListProperty>
#include <QtSql/QSqlDatabase>
#include <QtCore/QDebug>

class Book : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int id MEMBER id CONSTANT)
    Q_PROPERTY(QString title MEMBER title CONSTANT)
    Q_PROPERTY(QString path MEMBER path CONSTANT)
    Q_PROPERTY(bool hasCover MEMBER hasCover CONSTANT)
    Q_PROPERTY(QUrl cover READ cover CONSTANT)

public:
    Book(int id, QString title, QString path, bool hasCover, QObject *parent = nullptr)
        : QObject(parent), id(id), title(title), path(path), hasCover(hasCover) {}


    QUrl cover() const;

    int id;
    QString title;
    QString path;
    bool hasCover;
};

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

public slots:
    void refresh();

signals:
    void booksChanged();

private:
    QList<Book *> m_books;
    QSqlDatabase m_db;
};
