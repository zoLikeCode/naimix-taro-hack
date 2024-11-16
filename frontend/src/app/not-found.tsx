import Link from 'next/link';

const NotFound = () => {
  return (
    <div className="main__notfound">
      <p>Такая страница не найдена</p>
      <Link href="/">Вернуться на главную страницу</Link>
    </div>
  );
};

export default NotFound;
