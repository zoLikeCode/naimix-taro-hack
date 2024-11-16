import type { Metadata } from 'next';
import './fonts/Graphik/stylesheet.css';
import './globals.css';

export const metadata: Metadata = {
  title: 'TaroHack / MISIS GO',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru-RU">
      <head>
        <link rel="icon" href="./favicon.ico" sizes="any" />
      </head>
      <body>
        <header className="main__header">
          <nav></nav>
        </header>
        <main className="main__layout">{children}</main>
      </body>
    </html>
  );
}
