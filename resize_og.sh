#!/bin/bash
# OG 이미지를 1200x630px로 리사이즈하는 스크립트

INPUT="public/og-image.png"
OUTPUT="public/og-image.png"
TARGET_WIDTH=1200
TARGET_HEIGHT=630

if [ ! -f "$INPUT" ]; then
    echo "❌ 오류: $INPUT 파일을 찾을 수 없습니다."
    exit 1
fi

# 파일 크기 확인
FILE_SIZE=$(stat -f%z "$INPUT" 2>/dev/null || stat -c%s "$INPUT" 2>/dev/null)
if [ "$FILE_SIZE" -eq 0 ]; then
    echo "❌ 오류: 이미지 파일이 비어있습니다."
    echo "💡 이미지 파일을 다시 업로드하거나 확인해주세요."
    exit 1
fi

echo "🎨 OG 이미지 리사이즈 시작..."
echo "📁 입력 파일: $INPUT"
echo "💾 출력 파일: $OUTPUT"
echo "📐 목표 크기: ${TARGET_WIDTH}x${TARGET_HEIGHT}px"
echo "-" | sed 's/./─/g' | head -c 50 && echo

# 원본 크기 확인
ORIGINAL_SIZE=$(sips -g pixelWidth -g pixelHeight "$INPUT" 2>/dev/null | grep -E "pixelWidth|pixelHeight" | awk '{print $2}' | tr '\n' 'x' | sed 's/x$//')
echo "📸 원본 이미지 크기: ${ORIGINAL_SIZE}px"

# sips로 리사이즈 (비율 유지하면서 크롭)
# --resampleHeightWidthMax: 최대 크기 지정 (비율 유지)
# --cropToHeightWidth: 정확한 크기로 크롭
sips -z $TARGET_HEIGHT $TARGET_WIDTH "$INPUT" --out "$OUTPUT" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ 리사이즈 완료!"
    FINAL_SIZE=$(sips -g pixelWidth -g pixelHeight "$OUTPUT" 2>/dev/null | grep -E "pixelWidth|pixelHeight" | awk '{print $2}' | tr '\n' 'x' | sed 's/x$//')
    echo "📐 최종 크기: ${FINAL_SIZE}px"
    echo "✨ 완료! OG 이미지가 준비되었습니다."
else
    echo "❌ 리사이즈 실패"
    exit 1
fi

