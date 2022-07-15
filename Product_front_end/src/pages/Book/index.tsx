import { Table } from 'antd'
import { ApiFilled, PlusOutlined } from '@ant-design/icons';
import type { ActionType, ProColumns, ProDescriptionsItemProps } from '@ant-design/pro-components';
import {
    FooterToolbar,
    ModalForm,
    PageContainer,
    ProDescriptions,
    ProFormText,
    ProFormTextArea,
    ProTable,
} from '@ant-design/pro-components';
import { FormattedMessage, useIntl } from '@umijs/max';
import { Button, Drawer, Input, message } from 'antd';
import React, { useRef, useState } from 'react';
import type { FormValueType } from './components/UpdateForm';
import UpdateForm from './components/UpdateForm';
import { Get_all_books, search_books } from '@/services/ant-design-pro/api';

const Admin_Book: React.FC = () => {
    const [createModalVisible, handleModalVisible] = useState<boolean>(false);

    const [updateModalVisible, handleUpdateModalVisible] = useState<boolean>(false);

    const [showDetail, setShowDetail] = useState<boolean>(false);

    const actionRef = useRef<ActionType>();
    const [currentRow, setCurrentRow] = useState<API.RuleListItem>();
    const [selectedRowsState, setSelectedRows] = useState<API.RuleListItem[]>([]);

    const search_columns: ProColumns<API.RuleListItem>[] = [
        {
            title: "图书编号",
            dataIndex: 'bookID',
            valueType: 'digit',
            render: (dom, entity) => {
                return (
                    <a
                        onClick={() => {
                            setCurrentRow(entity);
                            setShowDetail(true);
                        }}
                    >
                        {dom}
                    </a>
                );
            },
        },
        {
            title: "名称",
            dataIndex: 'title',
            valueType: 'textarea',
            
        },
        {
            title: "作者",
            dataIndex: 'authors',
            valueType: 'textarea',
        },
        {
            title: "类别",
            dataIndex: 'categories',
            valueType: 'textarea',
        },
        {
            title: '操作',
            valueType: 'option',
            key: 'option',
            render: (text, record, _, action) => [
              <a
                key="editable"
                onClick={() => {
                  
                }}
              >
                编辑
              </a>,
              <a href="#" target="_blank" rel="noopener noreferrer" key="view">
                查看
              </a>,
            ],
          },
    ];

    return (
        <PageContainer>
            <ProTable<API.RuleListItem, API.PageParams>
                headerTitle="查询结果"
                actionRef={actionRef}
                rowKey="bookID"
                search={{
                    labelWidth: 120,
                }}
                toolBarRender={() => [
                    <Button
                        type="primary"
                        key="primary"
                        onClick={() => {
                            handleModalVisible(true);
                        }}
                    >
                        <PlusOutlined /> "增添新书"
                    </Button>,
                ]}
                onSubmit={async (values) => {
                    console.log("values",values)
                    // const search_book_msg = await search_books({...values as API.Book_search_options})
                    // console.log("msg",search_book_msg)
                }}
                request={async (values) => {
                    console.log(values)
                    if (values["bookID"] || values["title"] 
                    || values["authors"] || values["categories"]){
                        const data = await search_books({...values as API.Book_search_options});
                        console.log(data)
                        return{
                            success: data["success"],
                            data: data["data"]
                        }
                    }
                    const value = await Get_all_books();
                    console.log(value);
                    return {
                        success: true,
                        data: value as any,
                    }
                }}
                columns={search_columns}
                rowSelection={{
                    onChange: (_, selectedRows) => {
                        setSelectedRows(selectedRows);
                    },
                }}

            />
            
            {selectedRowsState?.length > 0 && (
                <FooterToolbar
                    extra={
                        <div>
                            {'已选择 '}
                            <a style={{ fontWeight: 600 }}>{selectedRowsState.length}</a>{' '}
                            {"项"}
                        </div>
                    }
                >
                    <Button
                        onClick={async () => {
                            // await handleRemove(selectedRowsState);
                            setSelectedRows([]);
                            actionRef.current?.reloadAndRest?.();
                        }}
                    >
                        批量删除
                    </Button>
                </FooterToolbar>
            )}
            <ModalForm
                title="新增书籍信息"
                width="400px"
                visible={createModalVisible}
                onVisibleChange={handleModalVisible}
                onFinish={async (value) => {
                    // const success = await handleAdd(value as API.RuleListItem);
                    const success = true
                    if (success) {
                        handleModalVisible(false);
                        if (actionRef.current) {
                            actionRef.current.reload();
                        }
                    }
                }}
            >
                <ProFormText
                    rules={[
                        {
                            required: true,
                            message: "必填项"
                        },
                    ]}
                    width="md"
                    name="name"
                />
                <ProFormTextArea width="md" name="desc" />
            </ModalForm>
            <UpdateForm
                onSubmit={async (value) => {
                    const msg={"success":true}
                    // console.log("value",value)
                    // const msg = await search_books();
                    if (msg["success"]) {                        
                        handleUpdateModalVisible(false);
                        setCurrentRow(undefined);
                        if (actionRef.current) {
                            actionRef.current.reload();
                        }
                    }
                }}
                onCancel={() => {
                    handleUpdateModalVisible(false);
                    if (!showDetail) {
                        setCurrentRow(undefined);
                    }
                }}
                updateModalVisible={updateModalVisible}
                values={currentRow || {}}
            />

            <Drawer
                width={600}
                visible={showDetail}
                onClose={() => {
                    setCurrentRow(undefined);
                    setShowDetail(false);
                }}
                closable={false}
            >
                {currentRow?.name && (
                    <ProDescriptions<API.RuleListItem>
                        column={2}
                        title={currentRow?.name}
                        request={async () => ({
                            data: currentRow || {},
                        })}
                        params={{
                            id: currentRow?.name,
                        }}
                        columns={search_columns as ProDescriptionsItemProps<API.RuleListItem>[]}
                    />
                )}
            </Drawer>
            {/* <Table bordered columns = {book_columns}
                size = "small" /> */}
        </PageContainer>
    );
};

export default Admin_Book