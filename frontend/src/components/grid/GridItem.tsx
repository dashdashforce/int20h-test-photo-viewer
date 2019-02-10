import * as React from 'react';
import styles from './Grid.module.css';

export interface GridItemProps {}

const GridItem: React.SFC<GridItemProps> = ({children}) => {
  return <div className={styles.item}>{children}</div>;
};

export default GridItem;
