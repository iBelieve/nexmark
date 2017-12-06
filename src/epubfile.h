#pragma once

#include <QtCore/QObject>
#include <QtXml/QDomDocument>

class KArchive;

class EPUBFile : public QObject {
    Q_OBJECT

public:
    ~EPUBFile();

public Q_SLOTS:

    void load(const QString &filename);

protected:
    void parseOPF();

    QDomDocument readDOM(const QString &filename);

private:
    KArchive *m_archive = nullptr;
};
