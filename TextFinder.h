#ifndef TEXTFINDER_H_
#define TEXTFINDER_H_

#include <QWidget>

namespace Ui {
class TextFinder;
}

class TextFinder: public QWidget {
  Q_OBJECT

 public:
  explicit TextFinder(QWidget *parent = 0);
  ~TextFinder();

 private slots:
    void on_button_find_clicked();

 private:
  Ui::TextFinder *ui;
  void load_test_file();
};

#endif // TEXTFINDER_H_
