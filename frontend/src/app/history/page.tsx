'use client';

import { useEffect, useState } from 'react';
import { Filtres, AttrbText, StaffBlock, AttrRasklText } from '../ui';
import css from './page.module.css';
import { GetTaros } from '../lib/getTaros';
import Link from 'next/link';

const Page = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const LoadProfiles = async () => {
      const response = await GetTaros();
      setHistory(response.result);
    };
    LoadProfiles();
  }, []);

  return (
    <div>
      <Filtres />
      <AttrRasklText />
      <div className={css.main__container}>
        {history.map((hst, index) => {
          return (
            <div key={index} className={css.main__content}>
              <span className={css.main__date}>17.11.2024</span>
              <span className={css.main__name}>{hst?.user_profile?.full_name}</span>
              <span className={css.main__prof}>{hst?.user_profile?.prof}</span>
              <span className={css.main_exp}>
                {hst?.user_profile?.experience +
                  (hst?.user_profile?.experience > 5
                    ? ' лет'
                    : hst?.user_profile?.experience < 2
                    ? ' год'
                    : ' года')}
              </span>
              <span className={css.city}>{hst?.user_profile?.city}</span>
              <Link href={`/users/${hst?.user_profile?.user_profile_id}`}>
                <button className={css.button} type="button">
                  Подробнее
                </button>
              </Link>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Page;
