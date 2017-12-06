#pragma once

#include <QtCore/QObject>
#include <QtCore/QUrl>

class BooksManager;

class Book : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int id MEMBER id CONSTANT)
    Q_PROPERTY(QString title MEMBER title CONSTANT)
    Q_PROPERTY(QString path MEMBER path CONSTANT)
    Q_PROPERTY(bool hasCover MEMBER hasCover CONSTANT)
    Q_PROPERTY(QUrl cover READ cover CONSTANT)

public:
    Book(int id, QString title, QString path, bool hasCover, QObject *parent = nullptr);

    QUrl cover() const;

    Q_INVOKABLE QString filename(const QString &format = "EPUB");

    int id;
    QString title;
    QString path;
    bool hasCover;
};
