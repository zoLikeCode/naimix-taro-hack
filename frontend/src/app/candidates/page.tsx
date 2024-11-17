'use client';

import { useEffect, useState } from 'react';
import { Filtres, AttrbText } from '../ui';
import { EmployeeInfo } from '../ui/employeeInfo/employeeInfo';
import css from './page.module.css';
import { useShowCount } from '../store';
import axios from 'axios';
import { GetAllProfiles } from '../lib/getAllProfiles';

const Page = () => {
  const [users, setUsers] = useState([]);
  const { count, setCount } = useShowCount();
  const [countPage, setCountPage] = useState(0);
  const [nowPage, setNowPage] = useState(0);

  useEffect(() => {
    const LoadProfiles = async () => {
      try {
        const profiles = await GetAllProfiles({ page: nowPage, limit: count });
        setUsers(profiles.result);
      } catch (error) {
        setUsers([]);
      }
    };
    LoadProfiles();
  }, [count, nowPage]);

  console.log(users);

  return (
    <div className={css.main__container}>
      <Filtres />
      <AttrbText />
      {users.map((user, index) => (
        <EmployeeInfo
          key={index}
          name={user?.full_name}
          id={user?.user_profile_id}
          salary={user?.salary}
          experience={
            user?.experience +
            (user?.experience > 5 ? ' лет' : user?.experience < 2 ? ' год' : ' года')
          }
          contacts={
            <span>
              <span>{user?.phone_number}</span>{' '}
              <span className={css.user__email}>{user?.email}</span> <span>{user?.city}</span>
            </span>
          }
        />
      ))}
    </div>
  );
};

export default Page;
