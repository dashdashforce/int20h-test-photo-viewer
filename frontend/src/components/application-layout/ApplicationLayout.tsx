import * as React from 'react';
import Header from '../header/Header';

import styles from './ApplicationLayout.module.css';

export interface ApplicationLayoutProps {
  children: React.ReactNode;
}

const ApplicationLayout: React.SFC<ApplicationLayoutProps> = ({children}) => {
  return (
    <div className={styles.block}>
      <div className={styles.header}>
        <Header />
      </div>
      <div className={styles.content}>{children}</div>
    </div>
  );
};

export default ApplicationLayout;
