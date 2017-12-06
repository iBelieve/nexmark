#include "epubfile.h"

#include <KZip>
#include <KArchiveDirectory>
#include <functional>
#include <QtCore/QDebug>

QDomElement findElement(const QDomDocument &doc, const QString &tagName,
                        std::function<bool(const QDomElement&)> filter)
{
    auto elements = doc.elementsByTagName(tagName);
    for (int i = 0; i < elements.count(); i++) {
        auto node = elements.at(i).toElement();
        if (filter(node)) {
            return node;
        }
    }

    return QDomElement();
}

EPUBFile::~EPUBFile()
{
    delete m_archive;
}

void EPUBFile::load(const QString &filename) {
    delete m_archive;
    m_archive = new KZip(filename);
    if (!m_archive->open(QIODevice::ReadOnly)) {
        qWarning() << "Unable to open EPUB:" << filename;
        return;
    }

    parseOPF();
}

void EPUBFile::parseOPF() {
    auto container = readDOM("META-INF/container.xml");
    auto rootFilename = findElement(container, "rootfile", [](auto element) {
        return element.attribute("media-type") == "application/oebps-package+xml";
    }).attribute("full-path");

    auto contents = readDOM(rootFilename);
}

QDomDocument EPUBFile::readDOM(const QString &filename) {
    QDomDocument doc;

    auto file = m_archive->directory()->file(filename);

    if (file == nullptr) {
        qWarning() << "File not found:" << filename;
        return doc;
    }

    auto dev = file->createDevice();

    doc.setContent(dev);
    dev->close();

    delete dev;

    return doc;
}
