import * as React from 'react';
import styles from './Grid.module.css';
import GridItem from './GridItem';

export interface GridProps {}

const Grid: React.SFC<GridProps> = ({children}) => {
  return <div className={styles.root}>{children}</div>;
};

export default Grid;
