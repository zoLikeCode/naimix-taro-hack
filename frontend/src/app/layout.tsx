import type { Metadata } from 'next';
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
      <body>{children}</body>
    </html>
  );
}
