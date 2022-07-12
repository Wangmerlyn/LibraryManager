import {Table} from 'antd'

const Borrow: React.FC = () =>{
    const columns=[
        {
            title: '图书编号',
            dataIndex: 'BookNum',
            key: 'BookNum',
        },
        {
            title: '图书名称',
            dataIndex: 'BookName',
            key: 'BookName',
        },
        {
            title: '作者',
            dataIndex: 'Writer',
            key: 'Writer',
        },
        {
            title: '类别ID',
            dataIndex: 'SortID',
            key: 'SortID'
        }
    ]    
    return (
        <div>
            <Table bordered columns = {columns}
                size = "small" />
        </div>
    );
};

export default Borrow