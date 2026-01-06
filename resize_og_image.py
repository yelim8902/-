#!/usr/bin/env python3
"""
OG 이미지를 1200x630px로 리사이즈하는 스크립트
"""
from PIL import Image
import os
import sys

def resize_og_image(input_path, output_path, target_size=(1200, 630)):
    """
    이미지를 OG 이미지 사이즈(1200x630px)로 리사이즈
    
    Args:
        input_path: 원본 이미지 경로
        output_path: 저장할 경로
        target_size: 목표 크기 (width, height)
    """
    try:
        # 이미지 열기
        if not os.path.exists(input_path):
            print(f"❌ 오류: {input_path} 파일을 찾을 수 없습니다.")
            return False
        
        img = Image.open(input_path)
        original_size = img.size
        print(f"📸 원본 이미지 크기: {original_size[0]}x{original_size[1]}px")
        
        # RGBA 모드로 변환 (투명도 지원)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # 비율을 유지하면서 리사이즈
        # 1200x630 비율: 약 1.905:1
        target_width, target_height = target_size
        target_ratio = target_width / target_height
        
        original_width, original_height = img.size
        original_ratio = original_width / original_height
        
        if original_ratio > target_ratio:
            # 원본이 더 넓음 → 높이 기준으로 리사이즈
            new_height = target_height
            new_width = int(target_height * original_ratio)
        else:
            # 원본이 더 높음 → 너비 기준으로 리사이즈
            new_width = target_width
            new_height = int(target_width / original_ratio)
        
        # 리사이즈 (고품질 리샘플링)
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        print(f"🔄 리사이즈 후: {new_width}x{new_height}px")
        
        # 1200x630 캔버스 생성 (중앙 정렬)
        canvas = Image.new('RGBA', target_size, (255, 255, 255, 0))
        
        # 중앙에 배치
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2
        canvas.paste(resized_img, (x_offset, y_offset), resized_img)
        
        # PNG로 저장
        canvas.save(output_path, 'PNG', optimize=True)
        print(f"✅ 저장 완료: {output_path}")
        print(f"📐 최종 크기: {target_width}x{target_height}px")
        
        return True
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False

if __name__ == "__main__":
    input_file = "public/og-image.png"
    output_file = "public/og-image.png"
    
    # 명령줄 인자로 다른 파일 지정 가능
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    print("🎨 OG 이미지 리사이즈 시작...")
    print(f"📁 입력 파일: {input_file}")
    print(f"💾 출력 파일: {output_file}")
    print("-" * 50)
    
    success = resize_og_image(input_file, output_file)
    
    if success:
        print("-" * 50)
        print("✨ 완료! OG 이미지가 1200x630px로 리사이즈되었습니다.")
    else:
        print("-" * 50)
        print("⚠️  실패했습니다. 이미지 파일을 확인해주세요.")
        sys.exit(1)

