'use client';

import './fonts/Graphik/stylesheet.css';
import './globals.css';
import Link from 'next/link';
import { PopupMenuNav } from './ui';
import { useState } from 'react';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [activeMenu, setActiveMenu] = useState<boolean>(true);
  return (
    <html lang="ru-RU">
      <head>
        <link rel="icon" href="./favicon.ico" sizes="any" />
        <title>TaroHack / MISIS GO</title>
      </head>
      <body>
        <header className="main__header">
          <nav className="main__nav">
            {/* <button
              type="button"
              className="main__header__button"
              onClick={() => {
                setActiveMenu(!activeMenu);
              }}
            >
              <div />
            </button> */}
            <Link href="/">
              <div className="main__header__logo" />
            </Link>
            <Link href="/candidates">
              <p className="main__back__text">Кандидаты</p>
            </Link>
            <Link href="/history">
              <p className="main__back__text">История раскладов</p>
            </Link>
          </nav>
        </header>
        <main className="main__layout">{children}</main>
      </body>
    </html>
  );
}
