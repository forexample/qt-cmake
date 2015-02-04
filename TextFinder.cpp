#include "TextFinder.h"
#include "ui_TextFinder.h"

#include <QFile>
#include <QTextStream>

TextFinder::TextFinder(QWidget *parent):
    QWidget(parent), ui(new Ui::TextFinder) {
  ui->setupUi(this);
  load_test_file();
}

TextFinder::~TextFinder() {
  delete ui;
}

void TextFinder::on_button_find_clicked() {
  const QString search_string(ui->lineEdit->text());
  ui->textEdit->find(search_string, QTextDocument::FindWholeWords);
}

void TextFinder::load_test_file() {
  QFile inputFile(":/input.txt");
  inputFile.open(QIODevice::ReadOnly);

  QTextStream in(&inputFile);
  const QString line = in.readAll();
  inputFile.close();

  ui->textEdit->setPlainText(line);
  QTextCursor cursor = ui->textEdit->textCursor();
  cursor.movePosition(QTextCursor::Start, QTextCursor::MoveAnchor, 1);
}
